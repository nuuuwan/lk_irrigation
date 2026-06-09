# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_05:38:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 05:38:12 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:33:59 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.014 |  |
| 2026-06-09 05:30:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:27:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-06-09 05:26:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | -0.032 |  |
| 2026-06-09 05:22:25 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:21:43 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.008 |  |
| 2026-06-09 05:20:19 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:16:46 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-06-09 05:13:23 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-06-09 05:12:32 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-06-09 05:10:43 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.028 |  |
| 2026-06-09 05:08:20 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-09 05:07:50 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.022 |  |
| 2026-06-09 05:06:36 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:06:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-09 05:05:36 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:05:31 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 05:05:09 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.097 |  |
| 2026-06-09 05:05:08 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 05:05:06 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.070 |  |
| 2026-06-09 05:04:40 | Putupaula (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-09 05:04:23 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:04:20 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-09 05:03:55 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 05:03:15 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.010 |  |
| 2026-06-09 05:02:53 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 05:02:30 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:02:28 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:02:24 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:02:02 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-06-09 05:02:00 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:01:43 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-09 05:01:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:01:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:01:08 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:00:38 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 05:08:20 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-09 05:06:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-09 05:02:53 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 05:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-09 05:01:43 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-09 05:05:08 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 05:05:31 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 05:05:36 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:00:38 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:01:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:20:19 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:01:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:38:12 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:30:55 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:01:08 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:04:23 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:02:30 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:03:55 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:02:00 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:02:24 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 05:21:43 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.008 |  |
| 2026-06-09 05:04:20 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-09 05:04:40 | Putupaula (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-09 05:03:15 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.010 |  |
| 2026-06-09 05:33:59 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.014 |  |
| 2026-06-09 04:10:54 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.018 |  |
| 2026-06-09 05:12:32 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-06-09 05:27:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-06-09 05:16:46 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-06-09 05:07:50 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.022 |  |
| 2026-06-09 05:10:43 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.028 |  |
| 2026-06-09 05:13:23 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-06-09 05:26:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | -0.032 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-09 05:05:06 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.070 |  |
| 2026-06-09 05:02:02 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-06-09 05:05:09 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)