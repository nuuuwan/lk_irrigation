# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_21:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 21:17:13 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.016 |  |
| 2026-06-20 21:08:18 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:08:14 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:07:29 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-06-20 21:07:08 | Glencourse (Kelani Ganga) | 9.78 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-20 21:07:08 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:06:38 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 21:06:27 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:06:08 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:05:33 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.239 |  |
| 2026-06-20 21:04:57 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:56 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:52 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-20 21:04:41 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.019 |  |
| 2026-06-20 21:04:37 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.023 |  |
| 2026-06-20 21:04:35 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:04:17 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-06-20 21:04:15 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:46 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:41 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-06-20 21:03:40 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.021 |  |
| 2026-06-20 21:03:20 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:15 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:11 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:09 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.051 |  |
| 2026-06-20 21:03:08 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:02:27 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:02:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.063 |  |
| 2026-06-20 21:01:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:21 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:14 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.035 |  |
| 2026-06-20 21:00:52 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 21:03:41 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-06-20 21:07:08 | Glencourse (Kelani Ganga) | 9.78 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-20 21:06:38 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-20 21:03:46 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:08 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:15 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:51 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:08:14 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:57 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:02:27 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:01:21 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:56 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:15 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:20 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:07:08 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:35 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:08:18 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:03:11 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:00:52 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 21:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-06-20 20:00:16 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:06:08 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-20 21:06:27 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-20 21:04:52 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-20 21:04:17 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-06-20 21:17:13 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.016 |  |
| 2026-06-20 21:04:41 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.019 |  |
| 2026-06-20 21:03:40 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.021 |  |
| 2026-06-20 21:04:37 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.023 |  |
| 2026-06-20 21:07:29 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-06-20 21:01:14 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.035 |  |
| 2026-06-20 21:03:09 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.051 |  |
| 2026-06-20 21:02:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.063 |  |
| 2026-06-20 21:05:33 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)