# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_11:35:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,184 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 11:35:40 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:34:48 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:11:57 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:11:15 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-15 11:10:27 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.057 |  |
| 2026-01-15 11:10:27 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:09:05 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:08:47 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 11:08:13 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-01-15 11:07:47 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.056 |  |
| 2026-01-15 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.035 |  |
| 2026-01-15 11:06:52 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-01-15 11:06:32 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-01-15 11:05:52 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 11:04:33 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:04:33 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-01-15 11:04:20 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:04:12 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-01-15 11:03:57 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:03:35 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:03:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-01-15 11:02:55 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.578 |  |
| 2026-01-15 11:02:47 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:46 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-01-15 11:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:19 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:10 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:56 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:55 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:34 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-01-15 11:01:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:28 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-15 11:01:22 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:21 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:19 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:00:34 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-15 11:00:20 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:00:10 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-15 10:58:46 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.578 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 11:08:47 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 11:05:52 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 11:11:15 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-15 11:02:47 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:22 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:56 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:03:35 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:10:27 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:11:57 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:03:57 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:55 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:21 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:09:05 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:04:33 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:04:20 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:01:19 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:19 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:00:20 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:10 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:35:40 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:34:48 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:06:52 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.009 |  |
| 2026-01-15 11:01:28 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-15 11:00:34 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-15 11:00:10 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-15 11:01:34 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-01-15 11:08:13 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-01-15 11:04:33 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-01-15 11:02:46 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-01-15 11:04:12 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-01-15 11:03:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-01-15 11:06:32 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-01-15 11:06:56 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.035 |  |
| 2026-01-15 11:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.056 |  |
| 2026-01-15 11:10:27 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.057 |  |
| 2026-01-15 11:02:55 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.578 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)