# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_14:17:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,949 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 14:17:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-02 14:17:18 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-05-02 14:15:03 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-05-02 14:14:09 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-05-02 14:13:23 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:11:08 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:10:06 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:09:16 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-02 14:08:34 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-02 14:07:52 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:07:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.102 |  |
| 2026-05-02 14:07:09 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.062 |  |
| 2026-05-02 14:06:39 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.147 |  |
| 2026-05-02 14:05:46 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:04:23 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:04:05 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 14:03:53 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:03:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:03:19 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 14:03:08 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-02 14:02:41 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-02 14:02:22 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.051 |  |
| 2026-05-02 14:02:21 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 14:02:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:51 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:42 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:36 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.021 |  |
| 2026-05-02 14:01:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:33 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-02 14:01:10 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-02 14:01:09 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-02 14:01:02 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.080 |  |
| 2026-05-02 14:00:59 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:00:52 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 14:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:00:41 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-02 14:00:39 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:00:26 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 14:02:41 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-02 14:08:34 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-02 14:01:09 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-02 14:09:16 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-02 14:00:41 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-02 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 14:17:56 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-02 14:03:19 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 14:00:52 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 14:04:05 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 14:02:21 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:04:23 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:42 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:36 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:07:52 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:05:46 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:11:08 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:10:06 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:01:51 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:03:46 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:02:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:13:23 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:00:26 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:03:53 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 14:17:18 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-05-02 14:14:09 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-05-02 14:01:33 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-02 14:01:10 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:12:43 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.015 |  |
| 2026-05-02 14:15:03 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-05-02 14:03:08 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-02 14:01:36 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.021 |  |
| 2026-05-02 14:02:22 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.051 |  |
| 2026-05-02 14:07:09 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.062 |  |
| 2026-05-02 14:01:02 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.080 |  |
| 2026-05-02 14:07:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.102 |  |
| 2026-05-02 14:06:39 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)