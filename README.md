# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_14:53:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,231 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 14:53:07 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:17:40 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.076 |  |
| 2026-04-20 14:16:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:12:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-20 14:10:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-04-20 14:10:18 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:09:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-20 14:08:05 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:08:00 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:07:50 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:07:30 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-20 14:06:35 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.106 |  |
| 2026-04-20 14:06:29 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:06:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:06:16 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-04-20 14:06:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:05:41 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 14:04:50 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-20 14:04:36 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:04:09 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-20 14:04:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-20 14:03:44 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:03:38 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:03:22 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:03:21 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:03:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:02:43 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 14:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 14:02:12 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 14:02:05 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.229 |  |
| 2026-04-20 14:01:25 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 14:01:19 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:01:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:01:07 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:01:03 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-04-20 14:01:01 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-04-20 14:01:00 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 14:06:16 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-04-20 14:09:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-20 14:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-20 14:12:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-20 14:07:30 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-20 14:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 14:04:50 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-20 14:02:12 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 14:01:25 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 14:05:41 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 14:04:36 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:03:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:16:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:04:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:03:21 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:53:07 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-20 13:00:52 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:01:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:01:07 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:06:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:06:29 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:07:50 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:08:00 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:08:05 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:03:38 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:10:18 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:06:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:04:09 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-20 14:02:43 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 14:03:22 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:03:44 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:01:00 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:01:19 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:10:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-04-20 14:01:03 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-04-20 14:01:01 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-04-20 14:17:40 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.076 |  |
| 2026-04-20 14:06:35 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.106 |  |
| 2026-04-20 14:02:05 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)