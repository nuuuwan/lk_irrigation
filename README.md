# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_10:18:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,512 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 10:18:41 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-04-07 10:11:03 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.105 |  |
| 2026-04-07 10:09:22 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.075 |  |
| 2026-04-07 10:09:13 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 10:09:13 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-04-07 10:08:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-07 10:07:14 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-04-07 10:07:05 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:06:26 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:06:23 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 10:06:19 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-04-07 10:06:04 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-04-07 10:05:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:05:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:05:23 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-07 10:05:12 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:04:57 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:04:48 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.069 |  |
| 2026-04-07 10:04:27 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | -0.058 |  |
| 2026-04-07 10:04:10 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:03:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:03:34 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-04-07 10:03:29 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-04-07 10:03:24 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-07 10:03:20 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2026-04-07 10:02:53 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.082 |  |
| 2026-04-07 10:02:14 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-04-07 10:02:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:02:05 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:01:31 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:01:24 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:01:22 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:01:22 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:00:59 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:00:54 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-07 10:00:06 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 10:08:26 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-04-07 10:05:23 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-07 10:00:06 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-07 10:09:13 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 10:06:23 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 10:01:22 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:05:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:04:57 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:03:20 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:00:59 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:02:05 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:04:10 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:01:31 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:07:05 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:05:12 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:05:54 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-07 10:06:19 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-04-07 10:01:24 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:02:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:03:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:06:26 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:01:22 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-07 10:07:14 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-04-07 10:02:14 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-04-07 10:03:24 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-07 10:00:54 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-07 10:18:41 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-04-07 10:09:13 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-04-07 10:03:34 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-04-07 10:06:04 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-04-07 10:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2026-04-07 10:04:27 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | -0.058 |  |
| 2026-04-07 10:04:48 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.069 |  |
| 2026-04-07 10:09:22 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.075 |  |
| 2026-04-07 10:03:29 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.080 |  |
| 2026-04-07 10:02:53 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.082 |  |
| 2026-04-07 10:11:03 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)