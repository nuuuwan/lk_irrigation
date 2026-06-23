# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_18:05:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:05:37 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 18:05:19 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:04:49 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-06-23 18:04:01 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-06-23 18:04:00 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.057 |  |
| 2026-06-23 18:03:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 18:03:27 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-23 18:03:09 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.129 |  |
| 2026-06-23 18:03:07 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.025 |  |
| 2026-06-23 18:03:05 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.049 |  |
| 2026-06-23 18:03:01 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:02:39 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:31 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.041 |  |
| 2026-06-23 18:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | -0.022 |  |
| 2026-06-23 18:02:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.054 |  |
| 2026-06-23 18:02:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:03 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.082 |  |
| 2026-06-23 18:02:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-06-23 18:01:56 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:01:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:55 | Ellagawa (Kalu Ganga) | 8.02 | 🟢 Normal | -0.040 |  |
| 2026-06-23 18:01:31 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:00:57 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:00:34 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.072 |  |
| 2026-06-23 18:00:07 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-06-23 18:00:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:24:41 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 18:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | -0.022 |  |
| 2026-06-23 17:03:58 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.039 |  |
| 2026-06-23 18:03:27 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-23 18:05:37 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 18:03:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 18:02:39 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:00:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:04:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:06:32 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:00:57 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:04:34 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:01:56 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:01:31 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:05:56 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:05:19 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:03:01 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:04:49 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-06-23 18:04:01 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-06-23 18:03:07 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.025 |  |
| 2026-06-23 18:02:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-06-23 18:00:07 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-06-23 18:01:55 | Ellagawa (Kalu Ganga) | 8.02 | 🟢 Normal | -0.040 |  |
| 2026-06-23 18:02:31 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.041 |  |
| 2026-06-23 18:03:05 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.049 |  |
| 2026-06-23 18:02:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.054 |  |
| 2026-06-23 18:04:00 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.057 |  |
| 2026-06-23 18:00:34 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.072 |  |
| 2026-06-23 17:05:18 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.072 |  |
| 2026-06-23 18:02:03 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.082 |  |
| 2026-06-23 17:15:33 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.089 |  |
| 2026-06-23 18:03:09 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.129 |  |
| 2026-06-23 17:06:02 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)