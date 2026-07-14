# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_14:24:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,052 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 14:24:22 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:18:03 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:17:57 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-14 14:17:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:15:10 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:13:12 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-07-14 14:10:46 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-07-14 14:09:05 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:09:01 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:08:33 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:08:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-14 14:07:32 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:07:05 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:07:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-14 14:07:02 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-14 14:06:05 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:05:39 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:04:46 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-07-14 14:04:11 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:04:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:03:49 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-14 14:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-14 14:03:43 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-14 14:03:34 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:03:12 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.107 |  |
| 2026-07-14 14:03:12 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-07-14 14:03:07 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:33 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:13 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:06 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:01 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 14:01:44 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.043 |  |
| 2026-07-14 14:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:01:34 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-07-14 14:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:01:24 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:01:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.175 |  |
| 2026-07-14 13:45:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 14:01:34 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-07-14 14:10:46 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-07-14 14:03:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-14 14:03:43 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-14 14:17:57 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-14 14:07:02 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-14 14:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-14 14:02:01 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 14:04:11 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:09:05 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:07:32 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 13:01:57 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:07:05 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:06 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:06:05 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:03:07 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:13 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:24:22 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:08:27 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:03:34 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:09:01 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:04:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:08:33 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:18:03 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:01:24 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:05:39 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:17:17 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 13:03:31 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:02:33 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 14:13:12 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-07-14 14:07:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-14 14:03:49 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-14 14:04:46 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-07-14 14:03:12 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-07-14 14:01:44 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.043 |  |
| 2026-07-14 14:03:12 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.107 |  |
| 2026-07-14 14:01:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)