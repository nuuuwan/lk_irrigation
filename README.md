# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_15:10:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 15:10:01 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:09:44 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:09:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:08:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:08:46 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.028 |  |
| 2026-06-24 15:07:31 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:05:54 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.083 |  |
| 2026-06-24 15:05:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:05:11 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:04:35 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.021 |  |
| 2026-06-24 15:04:23 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:04:17 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.058 |  |
| 2026-06-24 15:04:16 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.032 |  |
| 2026-06-24 15:04:15 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:04:06 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:04:04 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-06-24 15:04:03 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-06-24 15:03:52 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.049 |  |
| 2026-06-24 15:03:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:38 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.079 |  |
| 2026-06-24 15:03:03 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-06-24 15:03:02 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:00 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:02:54 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-06-24 15:02:33 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-06-24 15:02:30 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.064 |  |
| 2026-06-24 15:02:28 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-24 15:02:05 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:02:04 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 15:01:54 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-24 15:01:48 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:01:24 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:01:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:01:12 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.030 |  |
| 2026-06-24 15:00:32 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:00:25 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.022 |  |
| 2026-06-24 15:00:17 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 15:02:54 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-06-24 15:02:28 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-24 15:02:04 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 15:01:54 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-24 15:01:48 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:05:11 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:04:06 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:02:05 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:00:32 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:00 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:07:31 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:09:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:02 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:50 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:10:01 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:05:41 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:04:15 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 15:03:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:09:44 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:01:24 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:03:38 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:08:53 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:04:23 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:01:23 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-24 15:04:04 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-06-24 15:03:03 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2026-06-24 15:00:17 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.021 |  |
| 2026-06-24 15:04:35 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.021 |  |
| 2026-06-24 15:00:25 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.022 |  |
| 2026-06-24 15:08:46 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.028 |  |
| 2026-06-24 15:01:12 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.030 |  |
| 2026-06-24 15:04:16 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.032 |  |
| 2026-06-24 15:03:52 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.049 |  |
| 2026-06-24 15:04:03 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-06-24 15:04:17 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.058 |  |
| 2026-06-24 15:02:30 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.064 |  |
| 2026-06-24 15:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | -0.079 |  |
| 2026-06-24 15:05:54 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)