# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_15:12:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 15:12:45 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:11:38 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.100 |  |
| 2026-05-11 15:11:11 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-11 15:07:52 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 15:07:42 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:07:35 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:07:18 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-11 15:07:16 | Katharagama (Menik Ganga) | 2.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-11 15:07:07 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-11 15:06:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-05-11 15:05:52 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:05:51 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:05:44 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-05-11 15:05:27 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:05:12 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:04:54 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-11 15:04:48 | Thanamalwila (Kirindi Oya) | 2.30 | 🟢 Normal | -0.076 |  |
| 2026-05-11 15:04:22 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-05-11 15:03:41 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-11 15:03:39 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:26 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:03:22 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:22 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:10 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.078 |  |
| 2026-05-11 15:03:05 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:03 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 15:02:29 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 15:02:26 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:02:22 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.100 |  |
| 2026-05-11 15:02:01 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:01:51 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:01:46 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-11 15:01:11 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:01:11 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:01:10 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:00:51 | Thanthirimale (Malwathu Oya) | 2.85 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-11 15:00:33 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-11 15:00:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 15:01:46 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-11 15:07:07 | Moragaswewa (Deduru Oya) | 2.08 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-11 15:00:51 | Thanthirimale (Malwathu Oya) | 2.85 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-05-11 15:04:54 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-11 15:03:41 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-11 15:07:52 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 15:11:11 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-11 15:07:16 | Katharagama (Menik Ganga) | 2.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-11 14:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-11 15:07:18 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-11 15:02:29 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 15:03:03 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 15:07:42 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:02:26 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:05:52 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:12:45 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:07:03 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:05:51 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:07:35 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:00:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:01:11 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:01:11 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:05:12 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 15:03:05 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:22 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:39 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:05:27 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:03:22 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:02:01 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:01:10 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:01:51 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-11 15:00:33 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-11 15:05:44 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-05-11 15:04:22 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-05-11 15:06:36 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-05-11 15:04:48 | Thanamalwila (Kirindi Oya) | 2.30 | 🟢 Normal | -0.076 |  |
| 2026-05-11 15:03:10 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.078 |  |
| 2026-05-11 15:02:22 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.100 |  |
| 2026-05-11 15:11:38 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)