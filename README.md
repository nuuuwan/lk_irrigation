# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_16:17:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 16:17:25 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:17:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.008 |  |
| 2026-06-19 16:16:39 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:13:07 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.011 |  |
| 2026-06-19 16:11:11 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:11:03 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-06-19 16:10:25 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.091 |  |
| 2026-06-19 16:09:30 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:08:49 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-06-19 16:08:38 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:08:08 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 16:08:04 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-06-19 16:07:58 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:07:49 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.028 |  |
| 2026-06-19 16:07:19 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 16:07:19 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-19 16:01:56 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-19 16:08:08 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 16:06:27 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:02:25 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:00:13 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:16:39 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:04:24 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:01:21 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:01:26 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:17:25 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:09:30 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:04:14 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:06:05 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:08:38 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:03:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:07:58 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:06:53 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:11:11 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 16:17:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.008 |  |
| 2026-06-19 16:08:04 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-06-19 16:08:49 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.009 |  |
| 2026-06-19 16:02:20 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:03:10 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:00:11 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:03:36 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:03:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-19 16:13:07 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.011 |  |
| 2026-06-19 16:11:03 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.018 |  |
| 2026-06-19 16:01:06 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.021 |  |
| 2026-06-19 16:02:47 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-06-19 16:07:49 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.028 |  |
| 2026-06-19 16:04:18 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-06-19 16:04:43 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.039 |  |
| 2026-06-19 16:10:25 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)