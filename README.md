# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_14:29:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,823 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 14:29:57 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-04-24 14:28:40 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:21:39 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-04-24 14:14:11 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-04-24 14:09:06 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-04-24 14:08:28 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.055 |  |
| 2026-04-24 14:06:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-24 14:06:28 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.032 |  |
| 2026-04-24 14:06:25 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.035 |  |
| 2026-04-24 14:06:19 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:04:59 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 14:04:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:04:04 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-04-24 14:04:02 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:03:54 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:03:36 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.053 |  |
| 2026-04-24 14:03:35 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-24 14:03:26 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:03:14 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:03:11 | Katharagama (Menik Ganga) | 1.98 | 🟢 Normal | -0.039 |  |
| 2026-04-24 14:03:07 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.022 |  |
| 2026-04-24 14:03:01 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.37 | 🟢 Normal | -0.040 |  |
| 2026-04-24 14:02:45 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.063 |  |
| 2026-04-24 14:02:38 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-24 14:02:26 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:02:22 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-24 14:02:22 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-24 14:02:14 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:01:55 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:01:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-24 14:01:40 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-04-24 14:01:29 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.061 |  |
| 2026-04-24 14:01:17 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-24 14:01:02 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 14:00:59 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-24 14:00:41 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 14:00:59 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-04-24 14:03:35 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-24 14:01:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-24 14:02:22 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-24 14:06:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-24 14:01:02 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 14:04:59 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 14:04:26 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:03:01 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:28:40 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:02:26 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:06:19 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:02:14 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:03:54 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:00:41 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:14:11 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-04-24 14:09:06 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.009 |  |
| 2026-04-24 14:04:02 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:03:26 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:03:14 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:01:55 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-24 14:01:17 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-24 14:01:40 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-04-24 14:02:22 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-24 14:02:38 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-24 14:03:07 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.022 |  |
| 2026-04-24 14:21:39 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-04-24 14:29:57 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-04-24 14:06:28 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.032 |  |
| 2026-04-24 14:06:25 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.035 |  |
| 2026-04-24 14:03:11 | Katharagama (Menik Ganga) | 1.98 | 🟢 Normal | -0.039 |  |
| 2026-04-24 14:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.37 | 🟢 Normal | -0.040 |  |
| 2026-04-24 14:03:36 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.053 |  |
| 2026-04-24 14:08:28 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.055 |  |
| 2026-04-24 14:04:04 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-04-24 14:01:29 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.061 |  |
| 2026-04-24 14:02:45 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)