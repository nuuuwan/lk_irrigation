# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_18:20:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 18:20:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 18:17:31 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:17:14 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:14:40 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:13:38 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-05-02 18:12:23 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:11:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:08:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:07:47 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-02 18:07:42 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:05:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-05-02 18:05:09 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-02 18:05:03 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:04:33 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.028 |  |
| 2026-05-02 18:04:15 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:04:11 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:04:07 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.020 |  |
| 2026-05-02 18:03:32 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-05-02 18:03:22 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 18:03:06 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-05-02 18:03:05 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-05-02 18:02:49 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-02 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.070 |  |
| 2026-05-02 18:02:30 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.133 |  |
| 2026-05-02 18:02:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:02:10 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 18:01:43 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-02 18:01:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:38 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.085 |  |
| 2026-05-02 18:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 18:01:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:15 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 9.818 | 🔺 Rising |
| 2026-05-02 18:00:55 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:00:53 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 9.818 | 🔺 Rising |
| 2026-05-02 17:48:17 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 18:01:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 9.818 | 🔺 Rising |
| 2026-05-02 18:01:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-02 18:07:47 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-02 18:02:49 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 18:20:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 18:05:09 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-02 18:03:22 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-02 18:03:32 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:02:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:15 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:17:31 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:07:42 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:17:14 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:14:40 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:04:15 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:05:03 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:43 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:08:32 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:12:23 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:04:11 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:13:38 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:11:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:00:55 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:02:10 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-02 18:03:05 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-05-02 18:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-05-02 18:05:28 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-05-02 18:04:07 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.020 |  |
| 2026-05-02 18:04:33 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.028 |  |
| 2026-05-02 18:03:06 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-05-02 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.070 |  |
| 2026-05-02 18:01:38 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.085 |  |
| 2026-05-02 18:02:30 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)