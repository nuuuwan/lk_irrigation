# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_18:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 18:12:38 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-12 18:09:49 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 18:08:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 18:07:27 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:07:26 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.088 |  |
| 2026-05-12 18:07:06 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2026-05-12 18:06:41 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:05:40 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 18:05:31 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-12 18:04:26 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-05-12 18:04:11 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 18:04:05 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:03:53 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:03:42 | Moragaswewa (Deduru Oya) | 1.87 | 🟢 Normal | -0.108 |  |
| 2026-05-12 18:03:35 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:03:30 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 18:03:25 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.019 |  |
| 2026-05-12 18:03:22 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-05-12 18:03:16 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 18:03:11 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-05-12 18:03:08 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-05-12 18:02:52 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 18:02:51 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-12 18:02:43 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 18:02:28 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-05-12 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 18:02:11 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-12 18:02:04 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:02:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:01:53 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-12 18:01:49 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:01:41 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:01:38 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:01:29 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:00:39 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 18:03:22 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-05-12 18:04:26 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-05-12 18:03:08 | Dunamale (Aththanagalu Oya) | 2.16 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-05-12 18:03:11 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-05-12 18:01:53 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-05-12 18:02:51 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-12 18:05:31 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-12 18:02:11 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-12 18:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 18:05:40 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-12 18:02:52 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 18:12:38 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-12 18:03:16 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 18:04:11 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 18:09:49 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 18:03:30 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 18:08:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 18:01:41 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:04:05 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:01:29 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:02:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:03:53 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:07:27 | Thawalama (Gin Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-05-12 18:06:41 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:01:49 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:02:04 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:02:43 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-05-12 18:03:25 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.019 |  |
| 2026-05-12 18:03:35 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:00:39 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:02:28 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 18:07:06 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2026-05-12 18:07:26 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.088 |  |
| 2026-05-12 18:03:42 | Moragaswewa (Deduru Oya) | 1.87 | 🟢 Normal | -0.108 |  |
| 2026-05-12 17:07:41 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)