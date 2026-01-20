# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_17:16:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 17:16:27 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.008 |  |
| 2026-01-20 17:13:40 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.041 |  |
| 2026-01-20 17:13:32 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:09:28 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-01-20 17:08:32 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:08:14 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:07:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-20 17:07:14 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-01-20 17:06:56 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.058 |  |
| 2026-01-20 17:05:46 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:18 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:15 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-20 17:05:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 17:04:54 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-20 17:04:53 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:04:52 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:04:50 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:04:22 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:03:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:03:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-20 17:02:59 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:02:55 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:54 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 17:02:54 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-01-20 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:21 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:02:07 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:01:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-20 17:01:56 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-20 17:01:41 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:17 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:01 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:40 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 17:01:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-20 17:04:54 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-20 17:03:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-20 17:02:54 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 17:05:15 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-20 17:07:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-20 17:05:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 17:01:01 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:40 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:08:32 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:03:32 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:41 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:04:50 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:56 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:08:14 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:18 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:07 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:05:46 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:00:41 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:01:17 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:02:22 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 17:16:27 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.008 |  |
| 2026-01-20 17:09:28 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-01-20 17:07:14 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-01-20 17:02:54 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:55 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:01 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:04:22 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.010 |  |
| 2026-01-20 17:04:52 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:02:59 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:13:32 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-01-20 17:02:21 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:04:53 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-01-20 17:02:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-01-20 17:13:40 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.041 |  |
| 2026-01-20 17:06:56 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.058 |  |
| 2026-01-20 17:01:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)