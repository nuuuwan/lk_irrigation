# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_11:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 11:16:52 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:14:53 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:11:15 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:09:30 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:08:18 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:08:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-02 11:07:28 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:07:12 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 11:06:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-06-02 11:06:32 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-06-02 11:05:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:05:30 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.012 |  |
| 2026-06-02 11:04:25 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-02 11:04:22 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:03:59 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:03:58 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-06-02 11:03:45 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:03:27 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:03:27 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 11:03:23 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:02:59 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:02:17 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:02:08 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:02:00 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-06-02 11:01:42 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:01:37 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:01:20 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:01:09 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:00:39 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:00:29 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:00:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 11:00:20 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:00:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 10:59:36 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 11:08:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-02 11:04:25 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-02 11:03:27 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 11:00:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 11:02:08 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:00:29 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:02:59 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:00:39 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:05:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:01:20 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:07:28 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:04:22 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 10:59:36 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:00:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:02:17 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 10:05:36 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:08:18 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 10:05:21 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:11:15 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:09:30 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:16:52 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:03:45 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-02 11:06:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-06-02 11:06:32 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-06-02 11:03:23 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:07:12 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:03:59 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:01:09 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-02 11:03:58 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-06-02 11:02:00 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-06-02 11:05:30 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.012 |  |
| 2026-06-02 11:01:42 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:01:37 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:03:27 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-02 11:00:20 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)