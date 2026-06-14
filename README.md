# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_00:09:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,570 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 00:09:34 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-15 00:07:52 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.031 |  |
| 2026-06-15 00:07:04 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.019 |  |
| 2026-06-15 00:06:36 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.050 |  |
| 2026-06-15 00:06:00 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-15 00:05:38 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:05:15 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-06-15 00:05:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-15 00:04:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:57 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:03:50 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-15 00:03:45 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:27 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:21 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-15 00:03:14 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-06-15 00:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:02:56 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-15 00:02:34 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:02:24 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:02:17 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.088 |  |
| 2026-06-15 00:01:53 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:40 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:31 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:06 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:00:48 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:59:38 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.074 |  |
| 2026-06-14 23:40:20 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.026 |  |
| 2026-06-14 23:37:53 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 23:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.009 |  |
| 2026-06-15 00:06:00 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-15 00:05:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-15 00:03:50 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-15 00:03:21 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-14 23:06:54 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-15 00:01:31 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:40 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:00:48 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:05:38 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:04:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:02:24 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:45 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:01:53 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:27 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:37:53 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.007 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-15 00:02:56 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 00:09:34 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:04:53 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:03:54 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-14 23:14:01 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-06-15 00:07:04 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.019 |  |
| 2026-06-15 00:01:06 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-06-14 23:01:48 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:02:34 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:03:57 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:03:14 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-06-15 00:05:15 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-06-15 00:07:52 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.031 |  |
| 2026-06-15 00:06:36 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.050 |  |
| 2026-06-14 23:59:38 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.074 |  |
| 2026-06-15 00:02:17 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.088 |  |
| 2026-06-14 23:06:42 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)