# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_19:24:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,068 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 19:24:26 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:20:32 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.008 |  |
| 2026-06-17 19:15:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-17 19:14:36 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-06-17 19:09:22 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-06-17 19:08:35 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.045 |  |
| 2026-06-17 19:07:51 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:06:51 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:06:16 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.037 |  |
| 2026-06-17 19:06:00 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-06-17 19:05:08 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-06-17 19:04:50 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-06-17 19:04:46 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:04:39 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-06-17 19:04:33 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:04:07 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.061 |  |
| 2026-06-17 19:04:00 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-17 19:03:21 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-06-17 19:03:13 | Deraniyagala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.108 |  |
| 2026-06-17 19:03:11 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:03:04 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-17 19:02:53 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:49 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-17 19:02:42 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:40 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:20 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-17 19:02:19 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-17 19:02:05 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:01:52 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:01:35 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 19:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.095 |  |
| 2026-06-17 19:00:27 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:00:26 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:00:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 19:14:36 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-06-17 19:04:50 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-06-17 19:04:39 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-06-17 19:02:49 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-17 19:02:19 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-17 19:02:20 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-17 19:03:04 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-17 19:15:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-17 19:04:00 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-17 19:01:35 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:01:52 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:00:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:53 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:24:26 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:04:33 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:00:27 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:42 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:02:05 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:06:51 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:04:46 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:03:11 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:07:51 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:00:26 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 19:20:32 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.008 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 19:06:00 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-06-17 19:03:21 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:29 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-17 19:05:08 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-06-17 19:09:22 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-06-17 19:06:16 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.037 |  |
| 2026-06-17 19:08:35 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.045 |  |
| 2026-06-17 19:04:07 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.061 |  |
| 2026-06-17 19:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.095 |  |
| 2026-06-17 19:03:13 | Deraniyagala (Kelani Ganga) | 2.61 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)