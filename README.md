# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_05:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 05:12:12 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:12:11 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:12:10 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:12:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.107 |  |
| 2026-04-06 05:11:33 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-04-06 05:10:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-04-06 05:09:21 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 05:07:37 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-04-06 05:06:56 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-06 05:06:36 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:06:23 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:05:32 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-04-06 05:05:22 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:04:54 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 05:04:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:54 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:40 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 05:03:38 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:34 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:14 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.058 |  |
| 2026-04-06 05:03:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:05 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:02:39 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:02:32 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:02:13 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:01:51 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:01:43 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.048 |  |
| 2026-04-06 05:01:41 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-06 05:01:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-06 05:01:12 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:00:57 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-06 05:00:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:00:36 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 05:00:14 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-06 05:00:07 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-04-06 04:33:49 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:32:26 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 05:06:56 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-06 05:00:14 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-06 05:00:36 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-06 05:03:40 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-06 05:04:54 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 05:09:21 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 05:00:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:04:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:01:51 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:02:13 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:06:23 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:18 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:05 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:12:12 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:38 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:02:32 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:05:22 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:02:39 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:01:12 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:54 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:03:34 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:06:36 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 05:11:33 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-04-06 05:00:57 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:04:29 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-06 05:01:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-06 05:00:07 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-04-06 04:12:44 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-04-06 05:01:41 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-06 05:07:37 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-04-06 05:05:32 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-04-06 05:10:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-04-06 05:01:43 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.048 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-06 05:03:14 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.058 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-06 05:12:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)