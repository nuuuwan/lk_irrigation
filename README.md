# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_03:20:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,123 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 03:20:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -2.250 |  |
| 2026-06-20 03:19:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.84 | 🟢 Normal | -2.250 |  |
| 2026-06-20 03:19:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -2.250 |  |
| 2026-06-20 03:18:36 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-20 03:17:35 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:16:51 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:14:20 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.009 |  |
| 2026-06-20 03:13:29 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-06-20 03:12:18 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -288.000 |  |
| 2026-06-20 03:12:17 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -288.000 |  |
| 2026-06-20 03:12:15 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | -288.000 |  |
| 2026-06-20 03:12:14 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -288.000 |  |
| 2026-06-20 03:12:13 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -288.000 |  |
| 2026-06-20 03:10:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:10:02 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.058 |  |
| 2026-06-20 03:08:40 | Badalgama (Maha Oya) | 0.24 | 🟢 Normal | -2.032 |  |
| 2026-06-20 03:07:40 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:06:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-20 03:05:41 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:04:16 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-06-20 03:03:42 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:36 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-20 03:03:21 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:05 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.005 |  |
| 2026-06-20 03:02:42 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-06-20 03:02:25 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 03:02:22 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.042 |  |
| 2026-06-20 03:02:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:58 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:37 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:09 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.030 |  |
| 2026-06-20 03:00:55 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:54:21 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:39:05 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 03:06:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-20 03:02:25 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 03:03:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-20 03:18:36 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:16:51 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:00:55 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:37 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:42 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 23:00:15 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:21 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:01:58 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:42 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:02:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:10:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:03:18 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:17:35 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:36 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:05 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.005 |  |
| 2026-06-20 03:14:20 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.009 |  |
| 2026-06-20 03:05:41 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:07:40 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:13:29 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-06-20 02:05:13 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-20 02:06:24 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-06-20 03:02:42 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-06-20 03:04:16 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-06-20 03:01:09 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.030 |  |
| 2026-06-20 03:02:22 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.042 |  |
| 2026-06-20 03:10:02 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.058 |  |
| 2026-06-20 02:18:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -1.070 |  |
| 2026-06-20 03:08:40 | Badalgama (Maha Oya) | 0.24 | 🟢 Normal | -2.032 |  |
| 2026-06-20 03:20:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -2.250 |  |
| 2026-06-20 03:12:18 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -288.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)