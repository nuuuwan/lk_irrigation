# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_05:14:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,359 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 05:14:25 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.036 |  |
| 2026-04-25 05:12:18 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:11:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-25 05:10:28 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.033 |  |
| 2026-04-25 05:08:38 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:08:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-04-25 05:06:53 | Katharagama (Menik Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-04-25 05:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-04-25 05:05:37 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-25 05:05:34 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.064 |  |
| 2026-04-25 05:05:05 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-25 05:05:05 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-25 05:04:28 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-25 05:03:40 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:03:33 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-25 05:03:31 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.070 |  |
| 2026-04-25 05:03:10 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:03:09 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.020 |  |
| 2026-04-25 05:02:35 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-04-25 05:02:32 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:02:22 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:02:16 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.050 |  |
| 2026-04-25 05:01:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.036 |  |
| 2026-04-25 05:01:52 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:49 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:46 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:37 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 05:01:29 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | -0.050 |  |
| 2026-04-25 05:01:05 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:03 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-25 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:00:55 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-04-25 04:31:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 05:04:28 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-25 05:05:05 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-25 05:03:33 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 05:01:37 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 04:04:42 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 05:01:05 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:52 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:46 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 04:06:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:01:49 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:12:18 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 05:06:53 | Katharagama (Menik Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-04-25 05:05:37 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-04-25 05:08:38 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:02:32 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-25 04:04:08 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:03:40 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:02:22 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:03:10 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-04-25 05:02:35 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-04-25 05:08:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-04-25 05:11:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-25 05:03:09 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.020 |  |
| 2026-04-25 05:01:03 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-25 05:05:05 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-25 05:00:55 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-04-25 05:10:28 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.033 |  |
| 2026-04-25 05:14:25 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.036 |  |
| 2026-04-25 05:01:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.036 |  |
| 2026-04-25 05:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-04-25 05:02:16 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.050 |  |
| 2026-04-25 05:01:29 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | -0.050 |  |
| 2026-04-25 05:05:34 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.064 |  |
| 2026-04-25 05:03:31 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.070 |  |
| 2026-04-25 04:05:50 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -3.789 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)