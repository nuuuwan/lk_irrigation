# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_08:08:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 08:08:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:08:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.119 |  |
| 2026-04-05 08:07:42 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:06:19 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.144 |  |
| 2026-04-05 08:05:46 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:05:37 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.060 |  |
| 2026-04-05 08:05:19 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-05 08:05:18 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-05 08:05:16 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:04:52 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-04-05 08:04:19 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-04-05 08:04:13 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 08:04:08 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.040 |  |
| 2026-04-05 08:03:50 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:03:42 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:03:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.023 |  |
| 2026-04-05 08:03:07 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.058 |  |
| 2026-04-05 08:03:06 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:03:06 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 08:02:50 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-05 08:02:40 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-04-05 08:02:21 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:02:07 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.053 |  |
| 2026-04-05 08:01:46 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:01:45 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:01:33 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.025 |  |
| 2026-04-05 08:01:32 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-05 08:01:09 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.092 |  |
| 2026-04-05 08:01:04 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-04-05 08:00:56 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-05 08:00:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:00:35 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:00:31 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 08:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-05 08:00:12 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:37:46 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:28:56 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:26:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 08:01:32 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-05 07:04:35 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-05 08:05:19 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-05 08:04:13 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 08:03:06 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 08:02:50 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-05 08:00:31 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 07:07:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:03:42 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:01:46 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:00:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:01:45 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:05:46 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:02:21 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:00:12 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:05:16 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 07:12:38 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:07:42 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:03:50 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:08:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:03:06 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-04-05 08:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-05 08:05:18 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-05 08:00:56 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-05 08:02:40 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-04-05 08:04:52 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-04-05 08:04:19 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-04-05 07:02:09 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-04-05 08:03:27 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.023 |  |
| 2026-04-05 08:01:33 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.025 |  |
| 2026-04-05 08:04:08 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.040 |  |
| 2026-04-05 08:01:04 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-04-05 08:02:07 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.053 |  |
| 2026-04-05 08:03:07 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.058 |  |
| 2026-04-05 08:05:37 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.060 |  |
| 2026-04-05 08:01:09 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.092 |  |
| 2026-04-05 08:08:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.119 |  |
| 2026-04-05 08:06:19 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)