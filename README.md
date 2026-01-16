# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_08:23:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 08:23:56 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-01-16 08:13:03 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:12:59 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:11:04 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-16 08:11:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-16 08:10:28 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:10:05 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-16 08:08:09 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:07:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-16 08:06:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:06:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-16 08:06:27 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-16 08:06:22 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.121 |  |
| 2026-01-16 08:06:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:06:04 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.019 |  |
| 2026-01-16 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-16 08:05:00 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:05:00 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-16 08:04:54 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:04:10 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-01-16 08:04:09 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:04:07 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:03:43 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:03:30 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-01-16 08:03:29 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.072 |  |
| 2026-01-16 08:03:11 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-01-16 08:02:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-01-16 08:02:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:34 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-01-16 08:02:23 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:15 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 08:02:11 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-16 08:02:06 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:02 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:01:36 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.013 |  |
| 2026-01-16 08:01:08 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-01-16 08:01:00 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 08:02:34 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-01-16 08:05:00 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-16 08:02:11 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-16 08:05:16 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-16 08:06:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-16 08:10:05 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-16 08:11:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-16 08:02:15 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 08:02:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:03:11 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:01:00 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:04:54 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:12:59 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:06:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:23 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 07:37:02 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:04:09 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:02 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:02:06 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:06:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:08:09 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:04:07 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:03:43 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:05:00 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:13:03 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 08:07:38 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-16 08:06:27 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-16 08:11:04 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-16 08:01:08 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-01-16 08:01:36 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.013 |  |
| 2026-01-16 08:23:56 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-01-16 08:06:04 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.019 |  |
| 2026-01-16 08:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-01-16 08:03:30 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-01-16 08:02:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-01-16 08:03:29 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.072 |  |
| 2026-01-16 08:04:10 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.090 |  |
| 2026-01-16 08:06:22 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)