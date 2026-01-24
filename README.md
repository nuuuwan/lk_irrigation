# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_09:17:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,208 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 09:17:03 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:09:57 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:09:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:08:49 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:08:38 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:07:25 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:06:46 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:06:38 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:06:21 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:05:21 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.244 |  |
| 2026-01-24 09:04:38 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 09:04:33 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-24 09:04:32 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -4.966 |  |
| 2026-01-24 09:04:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:04:03 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -4.966 |  |
| 2026-01-24 09:03:55 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -4.966 |  |
| 2026-01-24 09:03:50 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.093 |  |
| 2026-01-24 09:03:41 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 09:03:29 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.040 |  |
| 2026-01-24 09:03:21 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:43 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | -0.039 |  |
| 2026-01-24 09:02:38 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:33 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 09:02:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-24 09:02:23 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:17 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:13 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-24 09:02:00 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-01-24 09:02:00 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:26 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.022 |  |
| 2026-01-24 09:01:25 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-24 09:01:23 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:16 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:15 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-01-24 09:01:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:11 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-24 09:01:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.093 |  |
| 2026-01-24 09:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 09:01:10 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-24 09:04:33 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-24 09:02:13 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-24 09:02:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-24 09:02:33 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 09:04:38 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 09:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 09:01:16 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:23 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:11 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:00 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:03:21 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:07:25 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:09:57 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:51 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:17 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:08:49 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:08:38 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:17:03 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:23 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:06:46 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:04:19 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:09:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:03:41 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:02:38 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:06:21 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:06:38 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 09:01:25 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-24 09:01:15 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-01-24 09:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-01-24 09:01:26 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.022 |  |
| 2026-01-24 09:02:43 | Weraganthota (Mahaweli Ganga) | -2.24 | 🟢 Normal | -0.039 |  |
| 2026-01-24 09:03:29 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.040 |  |
| 2026-01-24 09:02:00 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-01-24 09:03:50 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.093 |  |
| 2026-01-24 09:01:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.093 |  |
| 2026-01-24 09:05:21 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.244 |  |
| 2026-01-24 09:04:32 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -4.966 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)