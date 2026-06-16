# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_22:24:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,285 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 22:24:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:18:39 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.016 |  |
| 2026-06-16 22:18:08 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.008 |  |
| 2026-06-16 22:10:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-06-16 22:08:43 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-06-16 22:08:00 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.029 |  |
| 2026-06-16 22:06:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:06:34 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:06:07 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:05:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:05:29 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.048 |  |
| 2026-06-16 22:04:54 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-06-16 22:04:51 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:04:15 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.022 |  |
| 2026-06-16 22:04:12 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:04:10 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:04:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:04:00 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:55 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:49 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:33 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 22:03:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:29 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:20 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.051 |  |
| 2026-06-16 22:03:15 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:45 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:39 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.054 |  |
| 2026-06-16 22:02:28 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:20 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:11 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-06-16 22:02:05 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.034 |  |
| 2026-06-16 22:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:01:17 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 21:40:21 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 22:04:54 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-06-16 22:03:33 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 22:02:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:05:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:28 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:55 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:01:17 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:29 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:49 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:03:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:06:55 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:04:00 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:06:07 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:04:10 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:20 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:04:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:45 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:24:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:18:08 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.008 |  |
| 2026-06-16 22:06:34 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:03:15 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:04:12 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-16 21:02:23 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:04:51 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-16 22:18:39 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.016 |  |
| 2026-06-16 22:10:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-06-16 22:08:43 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-06-16 22:04:15 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.022 |  |
| 2026-06-16 22:08:00 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.029 |  |
| 2026-06-16 22:02:11 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-06-16 22:02:05 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.034 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-16 22:05:29 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.048 |  |
| 2026-06-16 22:03:20 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | -0.051 |  |
| 2026-06-16 22:02:39 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)