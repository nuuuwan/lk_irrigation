# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_19:20:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,335 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 19:20:02 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.008 |  |
| 2026-06-24 19:16:40 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:15:35 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.008 |  |
| 2026-06-24 19:10:51 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.009 |  |
| 2026-06-24 19:09:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:08:33 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.044 |  |
| 2026-06-24 19:07:16 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.028 |  |
| 2026-06-24 19:06:46 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-06-24 19:05:34 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-06-24 19:05:11 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-06-24 19:04:47 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.134 |  |
| 2026-06-24 19:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | -0.039 |  |
| 2026-06-24 19:04:21 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:03:51 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-06-24 19:03:50 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.028 |  |
| 2026-06-24 19:03:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-24 19:03:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:03:35 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:03:12 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:51 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:45 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:31 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 19:02:25 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:25 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.049 |  |
| 2026-06-24 19:02:25 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-06-24 19:02:23 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-24 19:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:12 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:11 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:11 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.041 |  |
| 2026-06-24 19:02:01 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-24 19:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:01:49 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:01:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:00:44 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.137 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 19:05:11 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-06-24 19:00:44 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-24 19:03:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-24 19:02:23 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-24 19:01:49 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:11 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:51 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:01:56 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:25 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:45 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:03:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:09:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:03:12 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:01:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:03:35 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:16:40 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:04:21 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:02:12 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 19:20:02 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.008 |  |
| 2026-06-24 19:15:35 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.008 |  |
| 2026-06-24 19:10:51 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.009 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 19:02:31 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 19:02:01 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:02:31 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-06-24 19:05:34 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-06-24 19:03:51 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-06-24 19:07:16 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.028 |  |
| 2026-06-24 19:03:50 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.028 |  |
| 2026-06-24 19:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | -0.039 |  |
| 2026-06-24 19:02:11 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.041 |  |
| 2026-06-24 19:08:33 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.044 |  |
| 2026-06-24 19:02:25 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.049 |  |
| 2026-06-24 19:06:46 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.059 |  |
| 2026-06-24 19:02:25 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-06-24 19:04:47 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)