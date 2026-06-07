# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_09:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,759 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 09:14:30 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 09:13:16 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:12:46 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-07 09:10:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.054 |  |
| 2026-06-07 09:10:38 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 09:07:07 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:06:14 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-06-07 09:06:09 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 12.343 | 🔺 Rising |
| 2026-06-07 09:06:07 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-07 09:05:47 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-06-07 09:05:45 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:05:06 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-07 09:05:06 | Rathnapura (Kalu Ganga) | 4.59 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-06-07 09:05:01 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-06-07 09:04:48 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.123 |  |
| 2026-06-07 09:04:31 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 09:04:19 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-07 09:04:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:46 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-06-07 09:03:24 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:22 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:17 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-06-07 09:03:10 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.212 |  |
| 2026-06-07 09:03:04 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-07 09:02:40 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:02:24 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-07 09:02:18 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:02:04 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 12.343 | 🔺 Rising |
| 2026-06-07 09:02:02 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:02:00 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-07 09:01:31 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:01:29 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.199 |  |
| 2026-06-07 09:01:12 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-06-07 09:00:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:00:45 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-07 09:00:18 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 12.343 | 🔺 Rising |
| 2026-06-07 09:00:08 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 09:06:09 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 12.343 | 🔺 Rising |
| 2026-06-07 09:06:14 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-06-07 09:05:06 | Rathnapura (Kalu Ganga) | 4.59 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-06-07 09:01:12 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-06-07 09:05:01 | Glencourse (Kelani Ganga) | 11.84 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-06-07 09:05:06 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-07 09:02:00 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-07 09:04:19 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-07 09:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-07 09:03:04 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-07 09:12:46 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-07 09:10:38 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 09:02:24 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-07 09:14:30 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 09:04:31 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 09:02:02 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:01:31 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:00:55 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:05:45 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 08:02:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:07:07 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:24 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:02:18 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:02:40 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:06:07 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:01:29 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:03:22 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:13:16 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-07 08:00:43 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 09:05:47 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-06-07 09:00:45 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-06-07 09:03:46 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-06-07 09:03:17 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-06-07 09:00:08 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.030 |  |
| 2026-06-07 09:10:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.054 |  |
| 2026-06-07 09:04:48 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.123 |  |
| 2026-06-07 09:01:28 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.199 |  |
| 2026-06-07 09:03:10 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)