# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_10:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,875 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 10:15:41 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.026 |  |
| 2026-05-20 10:12:23 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-05-20 10:08:12 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:08:00 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:07:27 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:06:53 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 10:06:28 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-20 10:05:49 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.048 |  |
| 2026-05-20 10:05:14 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.087 |  |
| 2026-05-20 10:04:43 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-05-20 10:04:21 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-20 10:04:04 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2026-05-20 10:03:55 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.022 |  |
| 2026-05-20 10:03:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 10:03:28 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 10:03:24 | Thanthirimale (Malwathu Oya) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-05-20 10:03:09 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-05-20 10:03:09 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 10:03:04 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:03:04 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:44 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:41 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-20 10:02:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:27 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-20 10:02:21 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-20 10:02:16 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:16 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:01:53 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.045 |  |
| 2026-05-20 10:01:50 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 10:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:01:20 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 10:01:09 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.031 |  |
| 2026-05-20 10:00:20 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.173 |  |
| 2026-05-20 10:00:15 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:00:10 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:58:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 10:06:28 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-20 10:01:50 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-20 10:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 10:03:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-20 10:03:28 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 10:01:20 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 10:06:53 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 10:00:15 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:00:10 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:16 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:03:09 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 09:11:18 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:03:04 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:44 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:03:04 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:08:12 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:04:21 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:07:27 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:08:00 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:02:16 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 10:12:23 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-05-20 10:02:27 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-20 10:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-20 10:02:21 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-05-20 10:04:43 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-05-20 10:03:24 | Thanthirimale (Malwathu Oya) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-05-20 10:02:41 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-20 10:03:55 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.022 |  |
| 2026-05-20 10:15:41 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.026 |  |
| 2026-05-20 10:03:09 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-05-20 10:01:09 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.031 |  |
| 2026-05-20 10:04:04 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2026-05-20 10:01:53 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.045 |  |
| 2026-05-20 10:05:49 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.048 |  |
| 2026-05-20 10:05:14 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.087 |  |
| 2026-05-20 10:00:20 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)