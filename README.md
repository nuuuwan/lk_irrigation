# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_12:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 12:17:30 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-03-14 12:11:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:10:13 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-03-14 12:08:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-14 12:08:21 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:08:08 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:06:25 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:06:10 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:06:02 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 12:05:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-14 12:04:31 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 12:04:17 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:04:16 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:04:11 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:03:45 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-14 12:03:18 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-03-14 12:03:18 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.041 |  |
| 2026-03-14 12:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-03-14 12:03:11 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-03-14 12:03:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:03:07 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.006 |  |
| 2026-03-14 12:03:05 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 12:03:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 12:02:48 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:02:42 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:02:41 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.107 |  |
| 2026-03-14 12:02:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:02:33 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 12:02:29 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 12:02:13 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 12:02:05 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.053 |  |
| 2026-03-14 12:02:02 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.011 |  |
| 2026-03-14 12:01:55 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:01:47 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-03-14 12:01:40 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-14 12:01:31 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:01:12 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:00:57 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 12:03:05 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 12:01:40 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-14 12:02:13 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 12:02:33 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 12:02:29 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 12:05:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-14 12:08:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-14 12:03:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 12:04:31 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 12:06:02 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 12:06:10 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:01:31 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:03:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:04:16 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:02:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:08:08 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:06:25 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:04:11 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:04:17 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:08:21 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:02:42 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:11:53 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:02:48 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:01:55 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:01:12 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:03:07 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.006 |  |
| 2026-03-14 12:17:30 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-03-14 12:00:57 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-14 12:03:45 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-14 12:03:11 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-03-14 12:02:02 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.011 |  |
| 2026-03-14 12:10:13 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-03-14 12:03:17 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-03-14 12:01:47 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-03-14 12:03:18 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-03-14 12:03:18 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.041 |  |
| 2026-03-14 12:02:05 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.053 |  |
| 2026-03-14 12:02:41 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)