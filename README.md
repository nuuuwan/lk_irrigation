# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_00:38:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 00:38:09 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.012 |  |
| 2026-05-20 00:14:55 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:14:37 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.005 |  |
| 2026-05-20 00:08:41 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-20 00:08:13 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.014 |  |
| 2026-05-20 00:07:14 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.012 |  |
| 2026-05-20 00:06:55 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:06:12 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-05-20 00:05:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-20 00:05:04 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:04:18 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:03:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:03:07 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:03:06 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-05-20 00:02:57 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:56 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:02:51 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:31 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:28 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-20 00:02:19 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-05-20 00:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.149 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 00:06:12 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-05-20 00:03:06 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-05-20 00:05:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-20 00:01:41 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-20 00:08:41 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-20 00:14:37 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.005 |  |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:19 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:05:04 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:57 | Moragaswewa (Deduru Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:07:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:01:57 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:14:55 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:01:35 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:01:54 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 23:01:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:00:32 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:02:51 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:03:23 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 00:03:07 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-19 23:05:33 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:06:55 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:04:18 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:02:56 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-20 00:02:19 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-05-20 00:07:14 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.012 |  |
| 2026-05-20 00:38:09 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.012 |  |
| 2026-05-20 00:08:13 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.014 |  |
| 2026-05-19 22:08:08 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.018 |  |
| 2026-05-20 00:02:28 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 23:58:49 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-05-20 00:01:12 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-05-19 21:18:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.052 |  |
| 2026-05-20 00:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)