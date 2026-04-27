# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_22:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,795 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 22:18:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-27 22:17:02 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-27 22:11:05 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:09:38 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-27 22:07:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.072 |  |
| 2026-04-27 22:07:14 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-04-27 22:06:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:05:36 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 22:05:28 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.055 |  |
| 2026-04-27 22:05:16 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 22:04:43 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 22:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.013 |  |
| 2026-04-27 22:04:32 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:04:26 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-27 22:04:23 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-27 22:04:19 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-27 22:03:41 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-04-27 22:03:27 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:03:19 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:03:06 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-27 22:02:58 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:02:49 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:02:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 22:02:34 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:02:18 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-04-27 22:02:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:02:09 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.071 |  |
| 2026-04-27 22:01:32 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-27 22:01:29 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.012 |  |
| 2026-04-27 22:01:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-04-27 22:01:12 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:01:02 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-27 22:00:48 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:00:44 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 21:54:24 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 22:02:18 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-04-27 22:03:41 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-04-27 22:01:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-04-27 22:01:02 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-27 22:01:32 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-27 22:03:06 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-27 22:04:23 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-27 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 22:05:16 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 22:04:43 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 22:02:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 22:05:36 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 22:09:38 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:06:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:02:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:03:27 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:00:44 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:03:19 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:11:05 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:02:34 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:01:12 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-27 22:17:02 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-27 22:02:58 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:02:49 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:00:48 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:04:32 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-27 22:01:29 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.012 |  |
| 2026-04-27 22:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.013 |  |
| 2026-04-27 22:04:19 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-27 22:04:26 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-27 22:18:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-27 22:07:14 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-04-27 22:05:28 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.055 |  |
| 2026-04-27 22:02:09 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.071 |  |
| 2026-04-27 22:07:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.072 |  |
| 2026-04-27 21:54:24 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)