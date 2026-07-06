# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_07:22:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 07:22:57 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:19:27 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:13:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:11:26 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.005 |  |
| 2026-07-06 07:10:35 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-06 07:09:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-07-06 07:08:41 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-07-06 07:08:34 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.019 |  |
| 2026-07-06 07:08:23 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-07-06 07:08:19 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:08:02 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:07:41 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:07:13 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:06:30 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 07:05:27 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.039 |  |
| 2026-07-06 07:05:05 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.015 |  |
| 2026-07-06 07:04:45 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.043 |  |
| 2026-07-06 07:04:27 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-07-06 07:04:21 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:04:15 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:04:08 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-07-06 07:04:07 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:04:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-07-06 07:03:49 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:03:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:03:21 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:03:12 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:02:59 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:02:47 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-06 07:02:33 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.102 |  |
| 2026-07-06 07:02:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:01:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:01:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-06 07:01:09 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-06 07:00:29 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 07:10:35 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-06 07:02:47 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-06 07:01:09 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-06 07:00:29 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-06 07:01:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-06 07:06:30 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 06:17:19 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-06 07:01:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:13:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:08:02 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:02:33 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:22:57 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:07:41 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:07:13 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:03:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:19:27 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:08:19 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:04:07 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:03:12 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 07:11:26 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.005 |  |
| 2026-07-06 07:08:23 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-07-06 07:04:15 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:03:49 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:03:21 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:04:21 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:02:59 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:02:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-06 07:04:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-07-06 07:05:05 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.015 |  |
| 2026-07-06 06:04:55 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.015 |  |
| 2026-07-06 07:08:34 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.019 |  |
| 2026-07-06 07:04:27 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-07-06 07:04:08 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-07-06 07:08:41 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-07-06 07:09:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-07-06 07:05:27 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.039 |  |
| 2026-07-06 07:04:45 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.043 |  |
| 2026-07-06 07:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)