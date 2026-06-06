# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_09:13:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 09:13:40 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:13:30 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.045 |  |
| 2026-06-06 09:10:24 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:07:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-06-06 09:07:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:07:08 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:06:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:05:49 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:05:30 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.011 |  |
| 2026-06-06 09:05:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-06 09:05:01 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:04:48 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-06-06 09:04:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:04:26 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.051 |  |
| 2026-06-06 09:04:18 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:04:07 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:03:44 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-06-06 09:03:40 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 09:03:39 | Putupaula (Kalu Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:03:20 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.021 |  |
| 2026-06-06 09:03:18 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.102 |  |
| 2026-06-06 09:03:15 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.010 |  |
| 2026-06-06 09:03:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-06 09:03:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:50 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-06-06 09:02:46 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:38 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:35 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:02:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:08 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:02:07 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-06-06 09:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 09:01:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:01:20 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:00:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:00:06 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 09:03:40 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 09:05:13 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-06 09:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 09:03:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-06 09:00:06 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:03:39 | Putupaula (Kalu Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:02:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:04:18 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:02:08 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 09:01:20 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:38 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:04:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:04:07 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:07:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:10:24 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:05:01 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:03:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:01:36 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:46 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:06:34 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:35 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:13:40 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:00:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:05:49 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-06-06 09:02:50 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-06-06 08:03:25 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-06 09:03:15 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.010 |  |
| 2026-06-06 09:05:30 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.011 |  |
| 2026-06-06 09:04:48 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-06-06 09:03:20 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.021 |  |
| 2026-06-06 09:03:44 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-06-06 09:02:07 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-06-06 09:13:30 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.045 |  |
| 2026-06-06 09:04:26 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.051 |  |
| 2026-06-06 09:07:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.062 |  |
| 2026-06-06 09:03:18 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.102 |  |
| 2026-06-06 08:02:11 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -2.042 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)