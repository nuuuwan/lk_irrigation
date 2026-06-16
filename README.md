# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_01:15:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 01:15:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:10:50 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-06-17 01:09:50 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 7.091 | 🔺 Rising |
| 2026-06-17 01:09:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:09:28 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:08:53 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-17 01:07:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:07:38 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 7.091 | 🔺 Rising |
| 2026-06-17 01:07:38 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-17 01:06:59 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-06-17 01:06:42 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-17 01:06:36 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.015 |  |
| 2026-06-17 01:05:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-06-17 01:05:16 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.043 |  |
| 2026-06-17 01:05:09 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:04:08 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 01:03:59 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:03:20 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.041 |  |
| 2026-06-17 01:03:11 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:59 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:41 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:32 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:24 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:01:54 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:01:49 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:01:35 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:01:21 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 01:09:50 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 7.091 | 🔺 Rising |
| 2026-06-17 01:08:53 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-17 01:06:42 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-17 00:03:58 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-17 01:04:08 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 00:04:58 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 01:07:38 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-17 01:07:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:59 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-17 00:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:01:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:03:11 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:01:21 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:41 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:01:54 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:32 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:15:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 00:11:27 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:09:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:01:49 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 01:02:24 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:24:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-06-17 00:16:34 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-06-17 01:10:50 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-06-17 01:09:28 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:01:35 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:03:59 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-17 01:05:09 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-17 00:01:36 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.012 |  |
| 2026-06-17 01:06:36 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.015 |  |
| 2026-06-17 00:06:03 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-06-17 01:05:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-06-17 01:06:59 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.038 |  |
| 2026-06-17 01:03:20 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.041 |  |
| 2026-06-17 01:05:16 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.043 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)