# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_15:10:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 15:10:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:09:57 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:09:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.053 |  |
| 2026-06-25 15:06:16 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:05:53 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:05:42 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:05:25 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:04:58 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:04:31 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:04:28 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.079 |  |
| 2026-06-25 15:04:11 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:04:11 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-06-25 15:04:05 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.020 |  |
| 2026-06-25 15:04:03 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:03:59 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:03:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 15:03:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-06-25 15:03:24 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:03:21 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.012 |  |
| 2026-06-25 15:02:48 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | -0.021 |  |
| 2026-06-25 15:02:46 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 15:02:38 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 15:02:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:02:36 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-06-25 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.079 |  |
| 2026-06-25 15:02:04 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:02:03 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 15:01:58 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:58 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:48 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:01:33 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:01:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:20 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:14 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.059 |  |
| 2026-06-25 15:00:47 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:00:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 15:02:38 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 15:03:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 15:02:46 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 15:02:03 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 15:00:47 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:09:57 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:10:17 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:04:58 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 14:01:19 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:02:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:05:53 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:05:42 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:05:25 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:21 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:03:59 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:58 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:04:31 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:06:16 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:58 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:03:24 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:20 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:02:04 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-25 15:01:48 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:04:11 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:00:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:01:33 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 15:04:03 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-25 14:09:16 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-06-25 15:03:21 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.012 |  |
| 2026-06-25 15:04:05 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | -0.020 |  |
| 2026-06-25 15:04:11 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-06-25 15:02:48 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | -0.021 |  |
| 2026-06-25 15:03:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-06-25 15:02:36 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.050 |  |
| 2026-06-25 15:09:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.053 |  |
| 2026-06-25 15:01:14 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.059 |  |
| 2026-06-25 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.079 |  |
| 2026-06-25 15:04:28 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)