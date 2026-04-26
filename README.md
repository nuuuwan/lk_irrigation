# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_22:28:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 22:28:06 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:25:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-26 22:15:07 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:13:44 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-26 22:09:15 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-26 22:08:30 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-26 22:07:39 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:07:31 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-26 22:06:34 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:05:56 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:05:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-04-26 22:04:39 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-26 22:04:37 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.028 |  |
| 2026-04-26 22:04:07 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 22:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:04:00 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-04-26 22:03:51 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:03:42 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:03:25 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:03:23 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-04-26 22:03:20 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 22:02:58 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-04-26 22:02:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:02:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-26 22:02:20 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 22:02:19 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.099 |  |
| 2026-04-26 22:02:11 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:02:02 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:01:59 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:01:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:01:25 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-04-26 22:00:42 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:13 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:11 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:09 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 22:04:00 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-04-26 21:04:27 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-26 22:25:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-26 22:04:39 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-26 22:02:20 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 22:07:31 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-26 22:04:07 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 22:03:20 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 22:08:30 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:11 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:01:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:03:51 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:15:07 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:42 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:01:59 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:02:02 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:09 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:00:13 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:02:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:05:56 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:02:11 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:07:39 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:06:34 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:28:06 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:03:42 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 22:13:44 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-26 22:09:15 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-26 22:03:23 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.010 |  |
| 2026-04-26 22:01:25 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-04-26 22:02:58 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-04-26 22:04:37 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.028 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-26 22:02:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-26 22:05:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-04-26 22:02:19 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.099 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)