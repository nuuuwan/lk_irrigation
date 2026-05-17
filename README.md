# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_21:31:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 21:31:09 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:16:00 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:07:58 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.056 |  |
| 2026-05-17 21:07:54 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-05-17 21:07:43 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.009 |  |
| 2026-05-17 21:07:07 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:06:15 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.013 |  |
| 2026-05-17 21:06:07 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:05:53 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.040 |  |
| 2026-05-17 21:05:40 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:05:09 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:04:52 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.022 |  |
| 2026-05-17 21:04:37 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:04:25 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | -0.069 |  |
| 2026-05-17 21:04:11 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.042 |  |
| 2026-05-17 21:03:39 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:03:32 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:03:21 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-17 21:03:09 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:03:01 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:02:56 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-05-17 21:02:30 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:02:25 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-05-17 21:02:24 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.060 |  |
| 2026-05-17 21:02:19 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:18 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-05-17 21:02:15 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:06 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:06 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-17 21:02:02 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.137 |  |
| 2026-05-17 21:01:48 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:01:37 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:01:37 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-05-17 21:01:13 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 7.826 | 🔺 Rising |
| 2026-05-17 21:00:50 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 7.826 | 🔺 Rising |
| 2026-05-17 21:00:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.064 |  |
| 2026-05-17 21:00:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 21:00:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.064 |  |
| 2026-05-17 21:01:13 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 7.826 | 🔺 Rising |
| 2026-05-17 21:02:06 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-17 21:03:21 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-17 21:00:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:03:09 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:19 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:31:09 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:03:32 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:01:37 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:01:48 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:04:37 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:06 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:15 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:05:09 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:07:07 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:05:40 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:07:43 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.009 |  |
| 2026-05-17 21:03:39 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:02:30 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:03:01 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:06:07 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:01:37 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-05-17 21:07:54 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-05-17 21:06:15 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.013 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-17 21:02:18 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-05-17 21:04:52 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.022 |  |
| 2026-05-17 21:02:56 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.031 |  |
| 2026-05-17 21:05:53 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.040 |  |
| 2026-05-17 21:02:25 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-05-17 21:04:11 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.042 |  |
| 2026-05-17 21:07:58 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.056 |  |
| 2026-05-17 21:02:24 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.060 |  |
| 2026-05-17 21:04:25 | Ellagawa (Kalu Ganga) | 7.23 | 🟢 Normal | -0.069 |  |
| 2026-05-17 21:02:02 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)