# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_08:22:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 08:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | -0.052 |  |
| 2026-05-10 08:18:04 | Moragaswewa (Deduru Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:13:45 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.028 |  |
| 2026-05-10 08:12:57 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-10 08:12:00 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:10:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-10 08:09:07 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:08:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 08:08:27 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.084 |  |
| 2026-05-10 08:07:00 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:06:55 | Katharagama (Menik Ganga) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-05-10 08:06:21 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:05:24 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.043 |  |
| 2026-05-10 08:05:14 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:04:26 | Moragaswewa (Deduru Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:04:07 | Kuda Oya (Kirindi Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:04:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:03:55 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-05-10 08:03:54 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:03:46 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.062 |  |
| 2026-05-10 08:03:25 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:03:23 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.024 |  |
| 2026-05-10 08:03:14 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-05-10 08:03:12 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-10 08:03:00 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:02:52 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-05-10 08:02:36 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |
| 2026-05-10 08:02:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:02:16 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | -0.039 |  |
| 2026-05-10 08:02:07 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.079 |  |
| 2026-05-10 08:02:06 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.050 |  |
| 2026-05-10 08:02:00 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:01:58 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-10 08:01:37 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.173 |  |
| 2026-05-10 08:01:37 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:01:31 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-05-10 08:01:19 | Kuda Oya (Kirindi Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:00:49 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.070 |  |
| 2026-05-10 08:00:07 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 08:08:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 08:10:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-10 08:18:04 | Moragaswewa (Deduru Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:05:14 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:06:21 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:03:54 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:03:25 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:09:07 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:02:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:04:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:03:00 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:02:00 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:01:37 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:12:00 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:07:00 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:04:07 | Kuda Oya (Kirindi Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 08:01:58 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-10 08:12:57 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-10 08:03:14 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-05-10 08:03:55 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-05-10 08:00:07 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-10 08:02:52 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-05-10 08:06:55 | Katharagama (Menik Ganga) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-05-10 08:03:23 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.024 |  |
| 2026-05-10 08:13:45 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.028 |  |
| 2026-05-10 08:03:12 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-10 08:01:31 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-05-10 06:04:35 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-10 07:03:25 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-05-10 08:02:16 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | -0.039 |  |
| 2026-05-10 08:05:24 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.043 |  |
| 2026-05-10 08:02:06 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.050 |  |
| 2026-05-10 08:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | -0.052 |  |
| 2026-05-10 08:03:46 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.062 |  |
| 2026-05-10 08:00:49 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.070 |  |
| 2026-05-10 08:02:07 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.079 |  |
| 2026-05-10 08:02:36 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |
| 2026-05-10 08:08:27 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.084 |  |
| 2026-05-10 08:01:37 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)