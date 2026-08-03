# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_08:06:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,605 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 08:06:54 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | -0.064 |  |
| 2026-08-03 08:06:41 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-03 08:06:35 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-08-03 08:05:59 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-03 08:05:53 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.074 |  |
| 2026-08-03 08:05:45 | Glencourse (Kelani Ganga) | 14.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 08:05:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-03 08:05:39 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:05:39 | Norwood (Kelani Ganga) | 2.02 | 🟡 Alert | -0.077 |  |
| 2026-08-03 08:05:27 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:05:22 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | 0.447 | 🔺 Rising |
| 2026-08-03 08:05:17 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:05:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-08-03 08:05:16 | Rathnapura (Kalu Ganga) | 6.60 | 🟡 Alert | -0.031 |  |
| 2026-08-03 08:04:57 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-03 08:03:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-03 08:03:50 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-03 08:03:26 | Peradeniya (Mahaweli Ganga) | 7.30 | 🟠 Minor Flood | -0.161 |  |
| 2026-08-03 08:03:18 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:03:15 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.172 |  |
| 2026-08-03 08:02:59 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-08-03 08:02:28 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:02:24 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:02:21 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 08:02:12 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:01:44 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 4.30 | 🟡 Alert | -1.258 |  |
| 2026-08-03 08:01:11 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:00:51 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 08:00:18 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-03 08:00:11 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-03 07:40:16 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 07:37:50 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | 0.062 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 08:03:26 | Peradeniya (Mahaweli Ganga) | 7.30 | 🟠 Minor Flood | -0.161 |  |
| 2026-08-03 08:05:16 | Rathnapura (Kalu Ganga) | 6.60 | 🟡 Alert | -0.031 |  |
| 2026-08-03 08:05:39 | Norwood (Kelani Ganga) | 2.02 | 🟡 Alert | -0.077 |  |
| 2026-08-03 08:01:16 | Nawalapitiya (Mahaweli Ganga) | 4.30 | 🟡 Alert | -1.258 |  |
| 2026-08-03 08:05:22 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | 0.447 | 🔺 Rising |
| 2026-08-03 08:02:59 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-08-03 08:03:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-03 08:05:59 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-03 08:06:41 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-03 08:00:18 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-03 08:05:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-03 08:04:57 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-03 08:02:21 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-03 08:00:11 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-03 08:00:51 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 08:05:45 | Glencourse (Kelani Ganga) | 14.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 07:04:08 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 07:15:19 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-03 07:05:58 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:01:44 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:05:39 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:05:17 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-03 06:07:35 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:05:27 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:02:28 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:02:12 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:02:24 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:01:11 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:03:18 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 08:06:35 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-08-03 08:03:50 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-03 07:04:11 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.035 |  |
| 2026-08-03 07:11:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.042 |  |
| 2026-08-03 08:06:54 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | -0.064 |  |
| 2026-08-03 08:05:53 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.074 |  |
| 2026-08-03 08:05:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.092 |  |
| 2026-08-03 07:06:12 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.157 |  |
| 2026-08-03 08:03:15 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)