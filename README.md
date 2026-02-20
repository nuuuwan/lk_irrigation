# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_11:06:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,099 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 11:06:26 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:05:58 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 11:05:50 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.029 |  |
| 2026-02-20 11:05:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-02-20 11:04:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:04:06 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:04:05 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-02-20 11:03:45 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:22 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-02-20 11:03:17 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-20 11:02:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:54 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:50 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.088 |  |
| 2026-02-20 11:02:35 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-20 11:02:06 | Weraganthota (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.119 |  |
| 2026-02-20 11:02:04 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.035 |  |
| 2026-02-20 11:01:42 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:12 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.040 |  |
| 2026-02-20 11:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:01 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:00:23 | Padiyathalawa (Maduru Oya) | 1.96 | 🟢 Normal | -1.290 |  |
| 2026-02-20 10:35:41 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 11:05:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-02-20 11:02:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-20 10:05:56 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-20 11:05:58 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 10:08:42 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-20 10:05:21 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 11:04:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:04:06 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:17 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 10:02:03 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:29 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:08 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:45 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:42 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:01 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:03:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 10:05:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 10:01:36 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:35 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:06:26 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:01:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:02:54 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 11:04:05 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-02-20 11:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-20 10:02:55 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-20 10:09:58 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-02-20 10:05:55 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-20 11:03:22 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-02-20 11:05:50 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.029 |  |
| 2026-02-20 11:02:04 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.035 |  |
| 2026-02-20 10:35:41 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |
| 2026-02-20 11:01:12 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.040 |  |
| 2026-02-20 11:02:50 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.088 |  |
| 2026-02-20 11:02:06 | Weraganthota (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.119 |  |
| 2026-02-20 11:00:23 | Padiyathalawa (Maduru Oya) | 1.96 | 🟢 Normal | -1.290 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)