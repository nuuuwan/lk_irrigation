# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_05:05:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 05:05:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:22 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.023 |  |
| 2026-06-20 05:05:18 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:36 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:35 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:06 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-20 05:02:40 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-06-20 05:02:24 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-06-20 05:02:12 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:06 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:51 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.015 |  |
| 2026-06-20 05:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:28 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:28 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.020 |  |
| 2026-06-20 05:01:21 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-20 05:01:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.161 |  |
| 2026-06-20 05:01:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:54 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:42 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:44:45 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:37:18 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:25:03 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.022 |  |
| 2026-06-20 04:22:00 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.015 |  |
| 2026-06-20 04:21:59 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.015 |  |
| 2026-06-20 04:21:58 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.015 |  |
| 2026-06-20 04:19:27 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.015 |  |
| 2026-06-20 04:19:25 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.015 |  |
| 2026-06-20 04:19:24 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.015 |  |
| 2026-06-20 04:16:59 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 04:05:15 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 2.270 | 🔺 Rising |
| 2026-06-20 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-20 05:01:21 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-20 04:02:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:42 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:54 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:40 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:06 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:04:36 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:59 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:18 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:10 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:12 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:05:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:37:18 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:01:28 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:05:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:14:38 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:08:23 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:06 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 05:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 05:01:51 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.015 |  |
| 2026-06-20 03:13:29 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-06-20 05:01:28 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.020 |  |
| 2026-06-20 04:25:03 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.022 |  |
| 2026-06-20 05:05:22 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.023 |  |
| 2026-06-20 04:01:17 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.024 |  |
| 2026-06-20 04:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.028 |  |
| 2026-06-20 05:02:24 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.030 |  |
| 2026-06-20 04:02:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-06-20 05:01:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)