# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_18:10:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 18:10:04 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-15 18:09:36 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.038 |  |
| 2026-06-15 18:08:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.149 |  |
| 2026-06-15 18:07:37 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:07:30 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:07:15 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.049 |  |
| 2026-06-15 18:07:09 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:06:49 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:06:32 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:05:42 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-06-15 18:05:19 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:05:00 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-15 18:04:25 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:03:43 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:03:31 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:03:20 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-06-15 18:03:20 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.030 |  |
| 2026-06-15 18:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.098 |  |
| 2026-06-15 18:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:54 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:46 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-06-15 18:02:44 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:35 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:28 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:22 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:21 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:15 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:01:41 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 18:01:16 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:00:57 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:56 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-06-15 18:00:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:33 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-06-15 18:00:21 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-15 18:00:10 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 18:10:04 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-15 18:00:21 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-15 18:05:00 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-15 18:03:04 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-15 18:01:41 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:56 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:03:43 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:44 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:06:32 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:07:09 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:22 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:06:49 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:35 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:07:37 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:00:57 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:21 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:05:19 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:54 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:07:30 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:04:25 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:28 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:15 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:01:16 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:05:42 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-06-15 18:00:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-06-15 18:00:33 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-06-15 18:03:20 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-06-15 18:03:20 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.030 |  |
| 2026-06-15 18:09:36 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.038 |  |
| 2026-06-15 18:00:10 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-06-15 18:07:15 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.049 |  |
| 2026-06-15 18:02:46 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-06-15 18:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.098 |  |
| 2026-06-15 18:08:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)