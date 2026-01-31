# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_18:21:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,848 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 18:21:05 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:13:08 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:13:03 | Manampitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-31 18:08:42 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:07:14 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 18:07:04 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-01-31 18:06:46 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:06:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 18:06:29 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:06:07 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 18:05:35 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:05:17 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:04:57 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-01-31 18:04:42 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:04:07 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:03:22 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-31 18:03:19 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:35 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:28 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-31 18:02:21 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:18 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-31 18:02:11 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-31 18:02:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:58 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:57 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 18:01:54 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.011 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:39 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-01-31 18:01:31 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.014 |  |
| 2026-01-31 18:01:28 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:01 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-31 18:00:42 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:00:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:00:09 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.045 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-31 18:01:01 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-31 18:03:22 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-31 18:06:35 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 18:13:03 | Manampitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-31 18:06:07 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 18:07:14 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 18:01:57 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 18:00:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:00:42 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:28 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:21 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:05:17 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:03:19 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:04:42 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:58 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:21:05 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:39 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:04:07 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:35 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:05:35 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:06:46 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:02:18 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:13:08 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:06:29 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:42 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-31 18:04:57 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-01-31 18:02:28 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-31 18:02:11 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-31 18:01:54 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.011 |  |
| 2026-01-31 18:01:31 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.014 |  |
| 2026-01-31 18:07:04 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-01-31 18:00:09 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.045 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-01-31 18:01:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)