# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_01:04:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 01:04:02 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 01:03:44 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.096 |  |
| 2026-01-06 01:03:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-06 01:03:00 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:58 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:36 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.052 |  |
| 2026-01-06 01:02:23 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:18 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-06 01:01:45 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:01:34 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 01:01:22 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-01-06 01:01:22 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-01-06 01:01:22 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:01:08 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-01-06 01:01:05 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-06 01:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:00:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-06 00:53:53 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 00:25:34 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 00:13:55 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-06 00:11:56 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 00:11:28 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-06 00:10:19 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.061 |  |
| 2026-01-06 00:09:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-06 00:09:00 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-01-06 00:08:34 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-01-06 00:08:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-06 00:07:02 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-06 00:06:56 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 00:09:00 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 4.154 | 🔺 Rising |
| 2026-01-06 00:06:00 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-01-05 23:06:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-06 00:09:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-06 00:13:55 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-06 01:01:34 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-06 00:11:56 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 01:02:18 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-06 00:01:00 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 00:03:06 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-06 00:02:11 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 01:04:02 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 00:11:28 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-06 01:01:05 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-06 01:01:45 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:58 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-06 00:03:43 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:03:00 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-05 23:00:10 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:01:22 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-06 00:25:34 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 00:08:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-06 01:02:23 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-06 00:04:36 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-01-06 01:03:38 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-06 00:07:02 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-06 01:01:08 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-01-06 00:03:53 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-01-06 01:01:22 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-01-06 01:00:53 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-01-06 01:01:22 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-01-06 01:02:33 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.052 |  |
| 2026-01-06 00:10:19 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.061 |  |
| 2026-01-06 01:03:44 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)