# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_06:31:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 06:31:29 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:27:56 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:23:41 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:18:48 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:11:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:10:15 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-05 06:08:10 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 06:07:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-05 06:06:49 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:05:39 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.020 |  |
| 2026-06-05 06:05:33 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 06:01:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-06-05 06:05:04 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-06-05 06:02:07 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-06-05 06:03:41 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-05 06:01:40 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-05 06:04:24 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-05 06:04:34 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 06:01:21 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-05 06:02:40 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-05 06:03:40 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 06:01:45 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 06:10:15 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-05 06:03:07 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 06:08:10 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 06:04:16 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 06:00:14 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-05 06:02:18 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 06:03:03 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-05 05:04:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:01:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:11:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:31:29 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:05:04 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:00:57 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:02:06 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:04:30 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:06:49 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:18:48 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:27:56 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:23:41 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-05 06:01:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-06-05 06:05:33 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | -0.010 |  |
| 2026-06-05 06:05:39 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.020 |  |
| 2026-06-05 06:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.021 |  |
| 2026-06-05 06:01:11 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.025 |  |
| 2026-06-05 06:07:18 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-05 06:02:58 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-06-05 06:03:28 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)