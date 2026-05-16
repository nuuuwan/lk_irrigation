# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_12:01:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 12:01:56 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:48 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:41 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:32 | Thanthirimale (Malwathu Oya) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:31 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | -0.030 |  |
| 2026-05-16 12:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-05-16 12:01:15 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 12:01:09 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.052 |  |
| 2026-05-16 12:00:25 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-05-16 11:59:17 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.114 |  |
| 2026-05-16 11:17:07 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.114 |  |
| 2026-05-16 11:09:08 | Galgamuwa (Mee Oya) | 3.57 | 🟢 Normal | -0.029 |  |
| 2026-05-16 11:08:55 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.039 |  |
| 2026-05-16 11:08:54 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.018 |  |
| 2026-05-16 11:08:50 | Rathnapura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.037 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 11:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 11:03:50 | Dunamale (Aththanagalu Oya) | 4.26 | 🟡 Alert | -0.041 |  |
| 2026-05-16 11:01:18 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-16 11:01:46 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-16 10:01:27 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-16 11:03:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-16 12:01:15 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 11:05:49 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-16 11:07:41 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 12:01:56 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:03:25 | Moragaswewa (Deduru Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:41 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:01:21 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:03:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:04:40 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:32 | Thanthirimale (Malwathu Oya) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:04:25 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:02:22 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 12:01:48 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 11:06:34 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-16 11:04:38 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-16 11:02:49 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-05-16 11:01:19 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-16 11:08:54 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.018 |  |
| 2026-05-16 11:01:16 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-05-16 12:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-05-16 11:02:11 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-05-16 11:09:08 | Galgamuwa (Mee Oya) | 3.57 | 🟢 Normal | -0.029 |  |
| 2026-05-16 11:05:27 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | -0.029 |  |
| 2026-05-16 12:01:31 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | -0.030 |  |
| 2026-05-16 12:00:25 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-05-16 11:08:50 | Rathnapura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.037 |  |
| 2026-05-16 11:08:55 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.039 |  |
| 2026-05-16 12:01:09 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.052 |  |
| 2026-05-16 11:02:57 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.052 |  |
| 2026-05-16 11:05:03 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.068 |  |
| 2026-05-16 11:05:33 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.081 |  |
| 2026-05-16 11:02:35 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.094 |  |
| 2026-05-16 11:59:17 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)