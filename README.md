# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_16:13:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 16:13:37 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-11 16:10:58 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 16:10:51 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 16:10:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:09:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-11 16:08:11 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-11 16:07:51 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:07:15 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 16:06:37 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.028 |  |
| 2026-06-11 16:06:33 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:06:24 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:06:08 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 16:06:02 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:05:07 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:05:01 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:05:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:05:00 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.014 |  |
| 2026-06-11 16:04:51 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-06-11 16:04:49 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.048 |  |
| 2026-06-11 16:04:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:28 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 16:04:25 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:04:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:13 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:09 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 16:04:00 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-06-11 16:03:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:03:46 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:03:32 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 16:02:59 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-11 16:02:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:02:37 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-06-11 16:02:34 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 16:02:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:02:07 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:00:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.122 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 16:02:37 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-06-11 16:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-11 16:08:11 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-11 16:04:28 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 16:09:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-11 16:13:37 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-11 16:02:59 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-11 16:02:34 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 16:10:58 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 16:03:32 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 16:04:09 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 16:07:15 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 16:04:25 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:02:07 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:03:46 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 16:06:08 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 16:10:51 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-11 16:05:07 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 15:03:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:05:01 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:06:33 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:13 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:03:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:06:24 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:00:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:07:51 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:02:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:06:02 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-11 15:00:17 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:10:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:02:27 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 16:04:00 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-06-11 16:05:00 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.014 |  |
| 2026-06-11 16:04:51 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-06-11 16:06:37 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.028 |  |
| 2026-06-11 16:04:49 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)