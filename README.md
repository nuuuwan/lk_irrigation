# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_03:16:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,450 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 03:16:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:14:06 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.034 |  |
| 2026-06-17 03:11:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-17 03:10:45 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:10:31 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.207 |  |
| 2026-06-17 03:09:33 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:08:28 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -4.235 |  |
| 2026-06-17 03:08:11 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:08:11 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -4.235 |  |
| 2026-06-17 03:07:02 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:06:37 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.023 |  |
| 2026-06-17 03:06:31 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:06:21 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-06-17 03:05:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-17 03:05:03 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-17 03:05:00 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.024 |  |
| 2026-06-17 03:04:51 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-17 03:04:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:04:23 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-06-17 03:04:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.136 |  |
| 2026-06-17 03:04:00 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-17 03:03:32 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-17 03:03:29 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 03:03:19 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-17 03:03:16 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:02:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:02:25 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.040 |  |
| 2026-06-17 03:02:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-17 03:01:38 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-17 03:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:44:12 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:43:01 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-06-17 02:40:03 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.028 |  |
| 2026-06-17 02:39:11 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.034 |  |
| 2026-06-17 02:38:48 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 02:03:32 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-17 03:05:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-17 03:11:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-17 03:04:00 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-17 03:03:32 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-17 03:04:51 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-17 03:02:12 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-17 03:03:29 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 03:08:11 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:06:31 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:16:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:03:16 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:20:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:09:33 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:02:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:32 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:04:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:03:48 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:07:02 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:10:45 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:08:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:02:25 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:06:21 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-06-17 03:05:03 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-17 03:03:19 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-17 03:01:38 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-17 02:03:42 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-06-17 03:06:37 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.023 |  |
| 2026-06-17 03:05:00 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.024 |  |
| 2026-06-17 03:04:23 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-06-17 03:14:06 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.034 |  |
| 2026-06-17 03:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.040 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-17 03:04:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.136 |  |
| 2026-06-17 03:10:31 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.207 |  |
| 2026-06-17 03:08:28 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -4.235 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)