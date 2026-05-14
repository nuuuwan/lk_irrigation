# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_12:08:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 12:08:19 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:08:16 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.049 |  |
| 2026-05-14 12:08:02 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-14 12:07:17 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:07:08 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-14 12:06:55 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.023 |  |
| 2026-05-14 12:06:22 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-14 12:05:07 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 12:05:05 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | -0.030 |  |
| 2026-05-14 12:04:57 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.049 |  |
| 2026-05-14 12:04:48 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:04:47 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:04:46 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:04:45 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | -0.107 |  |
| 2026-05-14 12:04:38 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-05-14 12:04:13 | Rathnapura (Kalu Ganga) | 4.04 | 🟢 Normal | -0.050 |  |
| 2026-05-14 12:03:53 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-14 12:03:47 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:03:09 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-14 12:03:04 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.39 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 12:02:46 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:02:43 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-05-14 12:02:27 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 12:02:12 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-14 12:02:11 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.061 |  |
| 2026-05-14 12:02:09 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:02:04 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.124 | 🔺 Rising |
| 2026-05-14 12:02:03 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-14 12:02:02 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-05-14 12:01:38 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:01:24 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:01:24 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:01:07 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-14 12:00:35 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 12:00:33 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 12:00:17 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:00:10 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 12:02:04 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.124 | 🔺 Rising |
| 2026-05-14 12:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.39 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 12:03:09 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-14 12:07:08 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-14 12:08:02 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-14 12:02:03 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-14 12:03:53 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-14 12:00:35 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 12:02:12 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-14 12:06:22 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-14 12:02:27 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 12:05:07 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 12:00:33 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 12:07:17 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:01:24 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:01:38 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:04:48 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:02:09 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:08:19 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:01:24 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:03:47 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:02:46 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-14 12:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:00:17 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:04:46 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:04:47 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:03:04 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | -0.010 |  |
| 2026-05-14 12:00:10 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.020 |  |
| 2026-05-14 12:01:07 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-14 12:02:02 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-05-14 12:06:55 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.023 |  |
| 2026-05-14 12:05:05 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | -0.030 |  |
| 2026-05-14 12:04:38 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | -0.031 |  |
| 2026-05-14 12:02:43 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-05-14 12:08:16 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.049 |  |
| 2026-05-14 12:04:57 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | -0.049 |  |
| 2026-05-14 12:04:13 | Rathnapura (Kalu Ganga) | 4.04 | 🟢 Normal | -0.050 |  |
| 2026-05-14 12:02:11 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.061 |  |
| 2026-05-14 12:04:45 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)