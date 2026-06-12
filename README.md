# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_18:10:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 18:10:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:10:32 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-12 18:09:45 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:08:09 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.010 |  |
| 2026-06-12 18:08:06 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-12 18:07:52 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 18:07:28 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.047 |  |
| 2026-06-12 18:06:58 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 18:06:20 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | 0.506 | 🔺 Rising |
| 2026-06-12 18:06:11 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.051 |  |
| 2026-06-12 18:05:35 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-06-12 18:05:31 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:05:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-06-12 18:05:20 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 18:04:02 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:03:53 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.079 |  |
| 2026-06-12 18:03:52 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:03:46 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-12 18:03:34 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-12 18:03:15 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.042 |  |
| 2026-06-12 18:03:04 | Nawalapitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-06-12 18:02:44 | Deraniyagala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.715 | 🔺 Rising |
| 2026-06-12 18:02:43 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 18:02:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:02:20 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.024 |  |
| 2026-06-12 18:02:18 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-12 18:02:12 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.031 |  |
| 2026-06-12 18:02:09 | Giriulla (Maha Oya) | 2.44 | 🟢 Normal | -0.022 |  |
| 2026-06-12 18:01:58 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.041 |  |
| 2026-06-12 18:01:48 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:01:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:01:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:01:14 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:01:09 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-12 18:00:41 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-12 18:00:20 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 18:06:20 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | 0.506 | 🔺 Rising |
| 2026-06-12 18:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-06-12 18:01:58 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.041 |  |
| 2026-06-12 18:02:44 | Deraniyagala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.715 | 🔺 Rising |
| 2026-06-12 18:03:04 | Nawalapitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-06-12 18:05:35 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-06-12 18:08:06 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-12 18:00:41 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-12 18:03:46 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-12 18:01:09 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-12 18:02:18 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 18:10:32 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-12 18:02:43 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 18:07:52 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 18:06:58 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 18:01:14 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:05:31 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:02:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:01:48 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:09:45 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:05:20 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:10:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:01:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:02:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:03:52 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:04:02 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:03:34 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-12 18:08:09 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.010 |  |
| 2026-06-12 18:02:09 | Giriulla (Maha Oya) | 2.44 | 🟢 Normal | -0.022 |  |
| 2026-06-12 18:02:20 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | -0.024 |  |
| 2026-06-12 18:02:12 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.031 |  |
| 2026-06-12 18:00:20 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.031 |  |
| 2026-06-12 18:03:15 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.042 |  |
| 2026-06-12 18:07:28 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | -0.047 |  |
| 2026-06-12 18:06:11 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.051 |  |
| 2026-06-12 18:05:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-06-12 18:03:53 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)