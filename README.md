# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_14:05:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,341 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 14:05:48 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-05-07 14:05:44 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-07 14:05:33 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-05-07 14:05:33 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 1.317 | 🔺 Rising |
| 2026-05-07 14:05:29 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.047 |  |
| 2026-05-07 14:05:11 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 14:04:53 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-07 14:04:51 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:04:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:04:13 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.031 |  |
| 2026-05-07 14:04:01 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:03:55 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-07 14:03:54 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 14:03:51 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:03:12 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-05-07 14:02:53 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-07 14:02:53 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.062 |  |
| 2026-05-07 14:02:45 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-05-07 14:02:35 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 14:02:24 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-05-07 14:02:24 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-05-07 14:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 14:02:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-07 14:02:09 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-07 14:01:48 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:01:48 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.093 |  |
| 2026-05-07 14:01:31 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.057 |  |
| 2026-05-07 14:01:16 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:01:14 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 14:00:50 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:22:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-07 13:16:53 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:16:41 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 14:05:33 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | 1.317 | 🔺 Rising |
| 2026-05-07 13:22:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-07 14:02:14 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-07 14:04:53 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-07 14:03:55 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-07 14:05:11 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 14:03:54 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 14:05:44 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-07 14:02:35 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 14:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 14:01:14 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 14:04:01 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:04:51 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:02:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:03:27 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:02:09 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:04:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 13:07:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:01:16 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:01:48 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-07 14:05:48 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-05-07 14:00:50 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-07 14:02:53 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-07 13:07:15 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-05-07 14:05:33 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-05-07 14:02:24 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-05-07 14:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-07 14:02:24 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-05-07 14:02:45 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-05-07 13:05:41 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-05-07 14:04:13 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.031 |  |
| 2026-05-07 13:16:41 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.033 |  |
| 2026-05-07 14:05:29 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.047 |  |
| 2026-05-07 14:01:31 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.057 |  |
| 2026-05-07 13:04:06 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.062 |  |
| 2026-05-07 14:02:53 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.062 |  |
| 2026-05-07 14:01:48 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.093 |  |
| 2026-05-07 14:03:12 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-05-07 13:10:35 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)