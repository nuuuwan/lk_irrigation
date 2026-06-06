# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_22:20:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,369 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 22:20:34 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.008 |  |
| 2026-06-06 22:13:14 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:09:35 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.036 |  |
| 2026-06-06 22:07:38 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:07:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:07:02 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-06-06 22:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:05:39 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | -0.050 |  |
| 2026-06-06 22:05:37 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 22:05:17 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:05:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:04:58 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.030 |  |
| 2026-06-06 22:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-06-06 22:04:10 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.042 |  |
| 2026-06-06 22:04:00 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-06 22:03:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:03:49 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.052 |  |
| 2026-06-06 22:03:28 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-06-06 22:03:18 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:03:05 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-06-06 22:02:47 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:02:33 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |
| 2026-06-06 22:02:08 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 22:01:58 | Ellagawa (Kalu Ganga) | 7.16 | 🟢 Normal | -0.050 |  |
| 2026-06-06 22:01:54 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:23 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:22 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 22:02:08 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 22:05:37 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 22:02:47 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:02:33 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:23 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:03:18 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:13:14 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:03:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:07:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:05:17 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:06:58 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:07:38 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:54 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:00:22 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:01:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 22:20:34 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.008 |  |
| 2026-06-06 22:07:02 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-06-06 22:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.009 |  |
| 2026-06-06 22:04:00 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-06 22:03:28 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-06-06 21:04:39 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-06-06 22:03:05 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-06-06 22:04:58 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.030 |  |
| 2026-06-06 22:09:35 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.036 |  |
| 2026-06-06 22:04:10 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.042 |  |
| 2026-06-06 22:01:58 | Ellagawa (Kalu Ganga) | 7.16 | 🟢 Normal | -0.050 |  |
| 2026-06-06 22:05:39 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | -0.050 |  |
| 2026-06-06 22:03:49 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.052 |  |
| 2026-06-06 22:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)