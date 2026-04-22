# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_10:31:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,869 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 10:31:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.014 |  |
| 2026-04-22 10:11:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:10:15 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-04-22 10:08:53 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-04-22 10:08:40 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:08:21 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:07:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:07:00 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.037 |  |
| 2026-04-22 10:06:50 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-04-22 10:06:37 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:05:39 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-04-22 10:05:27 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-22 10:05:25 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.086 |  |
| 2026-04-22 10:05:22 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.028 |  |
| 2026-04-22 10:05:14 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 10:04:57 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.038 |  |
| 2026-04-22 10:03:24 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:03:19 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:03:16 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-04-22 10:03:15 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:03:09 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.326 |  |
| 2026-04-22 10:03:05 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:03:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-04-22 10:02:45 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:02:42 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:02:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:02:37 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:02:32 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.050 |  |
| 2026-04-22 10:02:28 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:02:25 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:02:25 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.011 |  |
| 2026-04-22 10:02:18 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 10:02:08 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-22 10:01:49 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:24 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:08 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:01:06 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:00:51 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 10:05:27 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-22 10:02:18 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 10:02:08 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-22 10:05:14 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 10:00:51 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:02:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:49 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:24 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:03:05 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:01:06 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:03:19 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:02:45 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:08:40 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:11:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-22 10:08:53 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-04-22 10:07:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:06:37 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:02:25 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:02:37 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:03:15 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-22 10:02:25 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.011 |  |
| 2026-04-22 10:03:16 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-04-22 10:31:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.014 |  |
| 2026-04-22 10:10:15 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-04-22 10:01:08 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:03:24 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:02:28 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:02:42 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-22 10:05:22 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.028 |  |
| 2026-04-22 10:05:39 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-04-22 10:03:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-04-22 10:06:50 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-04-22 10:07:00 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.037 |  |
| 2026-04-22 10:04:57 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.038 |  |
| 2026-04-22 10:02:32 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.050 |  |
| 2026-04-22 10:05:25 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.086 |  |
| 2026-04-22 10:03:09 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.326 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)