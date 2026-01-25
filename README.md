# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_08:16:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,078 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 08:16:47 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:14:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.035 |  |
| 2026-01-25 08:12:43 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:09:27 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:07:10 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-25 08:07:03 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.042 |  |
| 2026-01-25 08:06:24 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:06:16 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:05:57 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.019 |  |
| 2026-01-25 08:05:54 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-01-25 08:05:50 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:05:42 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-01-25 08:05:28 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-25 08:05:17 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-25 08:05:14 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:05:04 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:04:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-01-25 08:04:41 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:04:38 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:04:20 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 08:04:18 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-25 08:03:54 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:03:44 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:03:16 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-25 08:03:01 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-25 08:02:56 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.012 |  |
| 2026-01-25 08:02:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |
| 2026-01-25 08:02:32 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:02:30 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 08:02:29 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 08:01:51 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:01:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:01:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.012 |  |
| 2026-01-25 08:01:00 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-25 08:00:51 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-01-25 08:00:42 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:00:24 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 08:00:22 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 08:05:17 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-25 08:01:00 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-25 08:04:20 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 08:03:01 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-25 08:02:30 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 08:02:29 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 08:00:24 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 08:05:28 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-25 08:00:42 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:00:22 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:05:04 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:04:41 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:06:16 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:09:27 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:12:43 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:03:44 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:16:47 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:02:32 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:03:54 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:01:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:05:14 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:01:51 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:06:24 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:04:38 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:05:50 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 08:04:18 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-25 08:07:10 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-25 08:03:16 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-25 08:05:42 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-01-25 08:04:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-01-25 08:01:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.012 |  |
| 2026-01-25 08:02:56 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.012 |  |
| 2026-01-25 08:05:57 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.019 |  |
| 2026-01-25 08:00:51 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-01-25 08:05:54 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-01-25 08:14:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.035 |  |
| 2026-01-25 08:07:03 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.042 |  |
| 2026-01-25 08:02:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)